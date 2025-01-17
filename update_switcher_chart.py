# EOL code, saving as this can be repurposed for a chart with the total translation progress

from datetime import datetime
from re import search

from git import Repo, GitCommandError
from matplotlib import pyplot
from matplotlib.ticker import PercentFormatter

repo = Repo('.')
progress, dates = [], []
for commit in repo.iter_commits():
    try:
        readme_content = repo.git.show('{}:{}'.format(commit.hexsha, 'README.md'))
    except GitCommandError:
        continue
    found = search(r'!\[(\d\d.\d\d)% przełącznika języków]', readme_content)
    if not found:
        found = search(r'!\[(\d+.\d\d)% language switchera]', readme_content)
    if not found:
        found = search(r'!\[(\d+.\d\d)% do language switchera]', readme_content)
    if not found:
        print(readme_content)
        continue
    number = float(found.group(1))
    progress.append(number)
    dates.append(datetime.fromtimestamp(commit.authored_date))

pyplot.plot_date(dates, progress, linestyle='-', marker='')
pyplot.ylim(ymin=0)
pyplot.grid()
pyplot.gcf().autofmt_xdate()
pyplot.gca().yaxis.set_major_formatter(PercentFormatter())
pyplot.title("Postęp tłumaczenia do dodania do przełącznika języków")
pyplot.savefig("language-switcher-progress.svg")
