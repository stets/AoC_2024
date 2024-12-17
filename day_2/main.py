class reports():
    def __init__(self):
        self.reports = []
        self.safe_reports_count = 0
        self.unsafe_reports_count = 0
        self.dampener_safe_reports = 0
        pass

    def open_reports(self):
        with open('input.txt', 'r') as file:
            for report in file:
                report = [int(x) for x in report.rstrip('\n').split()]
                self.reports.append(report)

    def _check_safety(self, report: list) -> bool:
        """"
        Returns True or False given a report
        Arguments:
        Report: <List> [1, 3, 5, 6]
        """
        order = 'undetermined'
        for idx, level in enumerate(report):
            if report[1] - report[0] > 0:
                order = 'increasing'
            if report[1] - report[0] < 0:
                order = 'decreasing'
            if report[1] - report[0] == 0:
                return False

            # if not first or last
            if idx > 0:
                # skip if not following order
                if report[idx] - report[idx-1] < 0 and order == 'increasing':
                    return False
                if report[idx] - report[idx-1] > 0 and order == 'decreasing':
                    return False
                # skip report if unsafe because increment was more than 2.
                if abs(report[idx] - report[idx - 1]) > 3:
                    return False
                # check if duplicate numbers.
                if level == report[idx-1]:
                    return False
        return True

    def check_all_reports(self):
        for report in self.reports:
            safe = self._check_safety(report)
            if safe:
                self.safe_reports_count += 1
        print(f"Safe Reports Count: {self.safe_reports_count}")

    def safety_dampener(self):
        for report in self.reports:
            safe = self._check_safety(report)
            if not safe:
                for idx, level in enumerate(report):
                    candidate = report.copy()
                    candidate.pop(idx)
                    safe = self._check_safety(candidate)
                    if safe:
                        self.safe_reports_count += 1
                        break

        print(f"Safe Reports with Safety Dampener turned on: {self.safe_reports_count}")


if __name__ == '__main__':
    reports = reports()
    reports.open_reports()
    reports.check_all_reports()
    reports.safety_dampener()
