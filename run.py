#!/usr/bin/env python3

import csv
import subprocess

space_id = "369535"

with open('solvers_divisions_final.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(data)
    for row in data:
        solver_id = row[1]
        solver_name = row[2]
        single_query_track = row[3]
        incremental_track = row[4]

        print(solver_name)

        if single_query_track:
            print('wrapping for single query track')
            p = subprocess.Popen(['./wrap_solver.sh', 'wrapped-sq', 'wrapper_sq', solver_id, space_id])
            p.communicate()
        if incremental_track:
            print('wrapping for incremental track')
            p = subprocess.Popen(['./wrap_solver.sh', 'wrapped-inc', 'wrapper_inc', solver_id, space_id])
            p.communicate()
