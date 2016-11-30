PSs=""
OUTS=""

for i in `seq 0 9`; do
    cmsRun runFlatTreeMINIAOD_SingleMuon_${i}_cfg.py &
    PSs="$PSs $!"
    OUTS="$OUTS output_${i}.root"
done

wait $PSs

hadd -f output_SingleMuon.root $OUTS

