# QA interview

1. python

there are 5 tests, checks web api
for run:
    Enter in cmdline(linux):
        cd python
        python3 -m pytest -v tests.py
    (Only first test crashes(Add new candidate without json header returns bad status))

2. datamining
get data processing results:
    Enter in cmdline(linux):
        cd datamining
        bash counter.sh 
        or 
        (type in console:
            echo "200 status code requests count: $(grep "\s200\s" datamining.log -c)" > datamining_results.log
         )(using bash scripting)