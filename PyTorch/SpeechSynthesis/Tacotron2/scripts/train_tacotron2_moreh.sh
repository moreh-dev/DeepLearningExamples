mkdir -p output.mo
python -m multiproc train.py -m Tacotron2 -d /home/share/dataset/tacotron2 -o ./output.mo/ -lr 1e-3 --epochs 1501 -bs 12 --weight-decay 1e-6 --grad-clip-thresh 1.0 --log-file molog.json --anneal-steps 500 1000 1500 --anneal-factor 0.1 --p-attention-dropout 0 --p-decoder-dropout 0
