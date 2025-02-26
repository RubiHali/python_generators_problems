import random
import time
from datetime import datetime


class RealTimeAnalytics:

    def stream_events(self):
        pages = ["home", "product", "search", "cart", "purchase"]
        user_ids = range(100, 200)
        while True:
            event = {
                "user_id": random.choice(user_ids),
                "page": random.choice(pages),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            yield event
            time.sleep(random.uniform(0.1, 0.5))

    def filter(self):
        for event in self.stream_events():
            if "purchase" in event["page"]:
                yield event

    def collect(self):
        purchase_events = []
        for event in self.filter():
            print(f"Processing user: {event['user_id']} visited {event['page']} at {event['timestamp']}")
            purchase_events.append(event)
            if len(purchase_events) >= 50:
                break
        print(f"\nCaptured 50 checkout events. Stopping.")
        return purchase_events


if __name__ == '__main__':
    real_time_analytics = RealTimeAnalytics()
    real_time_analytics.collect()
