from collections import defaultdict

class LogAnalyzer:

    def __init__(self):
        self.data = ''
        self.stats = {}

    def initiate(self, filepath: str):
        with open(filepath, 'r') as f:
            self.data = f.read()

    def analyze(self):

        if not self.data:
            print('No data loaded. Try initiating the file first.')
            return

        lines = self.data.splitlines()

        endpoint_hits = defaultdict(int)
        errors = 0
        total_requests = len(lines)
        time_response = defaultdict(int)

        for line in lines:
            line = line.split()

            if len(line) < 6:
                total_requests -= 1
                continue

            endpoint = line[3]
            code = line[4]
            timing = int(line[5].replace('ms', ''))

            endpoint_hits[endpoint] += 1
            time_response[endpoint] += timing

            if code.startswith(('4', '5')):
                errors += 1

        error_rate = round((errors / total_requests * 100), 2)
        sorted_endpoint_hits = dict(sorted(endpoint_hits.items(), key=lambda x:x[1], reverse=True))
        averages = {
            endpoint: round(time_response[endpoint] / hits, 1)
            for endpoint, hits in endpoint_hits.items()
        }

        self.stats = {
            'total': total_requests,
            'error_rate': error_rate,
            'endpoint_hits': sorted_endpoint_hits,
            'averages': averages
        }

    def report(self):
        if not self.stats:
            print('No data loaded. Try initializing the file first.')
            return

        print('----------------------------------------')
        print(f"Total requests: {self.stats['total']}")
        print("\nTop endpoints:")
        for endpoint, hits in self.stats["endpoint_hits"].items():
            print(f"  {endpoint} -> {hits} hits")

        print(f"\nError rate: {self.stats['error_rate']}%")
        print("\nAverage response times:")
        for endpoint, avg in self.stats["averages"].items():
            print(f"  {endpoint} -> {avg}ms")
        print('----------------------------------------')
