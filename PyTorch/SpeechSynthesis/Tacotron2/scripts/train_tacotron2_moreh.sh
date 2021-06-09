mkdir -p output.mo
python -m multiproc train.py -m Tacotron2 -o ./output.mo/ -lr 1e-3 --epochs 1501 -bs 48 --weight-decay 1e-6 --grad-clip-thresh 1.0 --log-file molog.json --anneal-steps 500 1000 1500 --anneal-factor 0.1
