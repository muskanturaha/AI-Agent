# spike_detector.py  (new)
from collections import deque
from datetime import datetime, timedelta
import pandas as pd

class SpikeDetector:
    """
    5‑minute rolling window.
    Evaluates once every `check_every` minutes (default 5).
    Stores window‑level stats to self.history and optional CSV.
    """

    def __init__(
        self,
        window_minutes:int = 5,
        thresh_neg_percent:float = 0.20,
        check_every:int = 5,
        callback=None,
        history_csv:str | None = "window_stats.csv"
    ):
        self.window        = deque()
        self.window_min    = window_minutes
        self.thresh        = thresh_neg_percent
        self.check_every   = check_every
        self.callback      = callback
        self.next_check    = None           # will be set on first add
        self.history_csv   = history_csv
        self.history       = []             # list of dicts

    def add(self, ticket:dict):
        now = ticket["timestamp"]
        self.window.append(ticket)

        # purge old
        cutoff = now - timedelta(minutes=self.window_min)
        while self.window and self.window[0]["timestamp"] < cutoff:
            self.window.popleft()

        # initialise next_check
        if self.next_check is None:
            self.next_check = (now.replace(second=0, microsecond=0)
                               + timedelta(minutes=self.check_every))

        # if it’s time to evaluate this window
        if now >= self.next_check:
            self._evaluate(now)
            self.next_check += timedelta(minutes=self.check_every)

    # ---------------------------------------------------------------------
    def _evaluate(self, now):
        total = len(self.window)
        neg_high = sum(
            1 for t in self.window
            if t["emotion"] in {"anger", "sadness"} and t["urgency"] == "high"
        )
        frac = neg_high / total if total else 0.0

        window_stat = {
            "window_end": now.strftime("%Y-%m-%d %H:%M"),
            "total":      total,
            "neg_high":   neg_high,
            "percent":    round(frac * 100, 2)
        }
        self.history.append(window_stat)

        # Persist for later RAG / dashboard
        if self.history_csv:
            pd.DataFrame(self.history).to_csv(self.history_csv, index=False)

        # Trigger Slack only if threshold breached
        if frac >= self.thresh and self.callback:
            self.callback(window_stat)

