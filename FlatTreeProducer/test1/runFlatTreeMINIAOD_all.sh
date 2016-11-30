PSs=""
OUTS=""

for i in `seq 0 8`; do
    cmsRun runFlatTreeMINIAOD_${i}_cfg.py &
    PSs="$PSs $!"
    OUTS="$OUTS output_${i}.root"
done

wait $PSs

hadd -f output.root $OUTS

