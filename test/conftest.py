import pytest
from _pytest.runner import TestReport
from _pytest.terminal import TerminalReporter
#import pprint
from pprint import pprint
from pathlib import Path
@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter):  # type: (TerminalReporter) -> generator
    yield
    # you can do here anything - I just print report info
    results = {}
    print('=' * 8 + 'CODESCHOOLUZ PYTHON' + '=' * 8)
    # print(dir(terminalreporter))

    for report in terminalreporter.stats.get('passed',[]):
        #Get from report task name and assign to task_name
        task_name = Path(report.location[0]).stem[5:]
        #Add task_name to dict results as key
        results.setdefault(task_name, {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'total': 0
        })
        #Increment passed
        results[task_name]['passed']+=1


    for report in terminalreporter.stats.get('failed',[]):
        #Get from report task name and assign to task_name
        task_name = Path(report.location[0]).stem[5:]

        #Add task_name to dict results as key
        results.setdefault(task_name, {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'total': 0
        })
        #Increment failed
        results[task_name]['failed']+=1
        report.nodeid ='\n'+task_name

    #Print readability report
    keys = sorted(results.keys())
    for task_name in keys:
        # task_name=results[t]
        task_results=results[task_name]
        if task_results['failed'] == 0:
            print(f'{task_name}  Passed:{task_results["passed"]} Failed:{task_results["failed"]} ✅')
        else:
            print(f'{task_name}  Passed:{task_results["passed"]} Failed:{task_results["failed"]} ❌')
    # for failed in terminalreporter.stats.get('failed', []):  # type: TestReport
    #     print(failed.location)
        
    #     #Test name
    #     print(failed.head_line)
    #     print(failed.nodeid)
        # failed.nodeid = failed.nodeid[-10:]
        # print(failed.longreprtext)
     

    # for passed in terminalreporter.stats.get('passed', []):  # type: TestReport
    #     print('passed! node_id:%s, duration: %s, details: %s' % (passed.nodeid,
    #                                                              passed.duration,
    #                                                              str(passed.longrepr)))