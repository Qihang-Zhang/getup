python3 ./python_scripts/merge_mkdocs.py

python3 ./python_scripts/generate_md.py \
--getup_threshold 7.75 \
--recent_days 30 \
--name Qihang
                      
mkdocs gh-deploy --force

git add .
git commit -m "$(date +%Y-%m-%d) update"
git push origin gh-pages:gh-pages
