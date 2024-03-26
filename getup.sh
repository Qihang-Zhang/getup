git pull
python3 generate_csv.py --cutoff 5

git add .
git commit -m "$(date +%Y-%m-%d) update"
git push

# below is to print some interesting message, feel free to delete or modify it
# echo "==========================================================================="
# echo "Morning! Have a nice day!"
# echo "==========================================================================="
# figlet Morning!
# figlet Have a nice day!
# echo "==========================================================================="
# sleep 2
# sl -h
