git clone https://github.com/Qihang-Zhang/getup-core.git

ln -s getup-core/* .

pip install -r requirements.txt

git pull
python3 generate_csv.py --cutoff 5

git add .
git commit -m "$(date +%Y-%m-%d) update"
git push

python3 ./python_scripts/merge_mkdocs.py

python3 ./python_scripts/generate_md.py \
--getup_threshold 6.75 \
--recent_days 30 \
--name Qihang
                      
mkdocs gh-deploy --force

git add .
git commit -m "$(date +%Y-%m-%d) update"
git push origin gh-pages:gh-pages
