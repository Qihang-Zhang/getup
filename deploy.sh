python3 ./python_scripts/merge_mkdocs.py

python3 ./python_scripts/generate_md.py \
--getup_threshold 6.75 \
--recent_days 30 \
--tz "America/Vancouver" \
--name Qihang
                      
mkdocs gh-deploy --force

git add .
git commit -m "$(date +%Y-%m-%d) update"
git push origin gh-pages:gh-pages
