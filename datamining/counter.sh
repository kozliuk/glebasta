#!/bin/bash
echo "200 status code requests count: $(grep "\s200\s" datamining.log -c)" > datamining_results.log
