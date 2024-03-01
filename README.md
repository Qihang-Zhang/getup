This is a project to document the time you get up everyday and visualize it in a website. It will document the first time when you type `getup` in your terminal everyday. The project is based on `mkdocs` and `mkdocs-material` package. The website is hosted on github page. To preview the website, please click [here](https://qihang-zhang.github.io/getup/).
## To make the project for your own:
1. fork the project to your own github account and ensure github action is enabled([English Version](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) or [Chinese Version](https://docs.github.com/zh/actions/using-workflows/disabling-and-enabling-a-workflow)).
2. git clone the forked project to your local.
3. **delete** the `data` folder
4. if you haven't install python3, please install python3 first: [python3](https://www.python.org/downloads/), [anaconda](https://www.anaconda.com/products/distribution) or [miniconda](https://docs.conda.io/en/latest/miniconda.html)
5. (optional)install the `sl` and `figlet` package
```shell
# if you are using mac, you can install sl by brew:
brew install sl
# if you are using linux, you can install sl by apt:
sudo apt-get install sl
# if you are using mac, you can install figlet by brew:
brew install figlet
# if you are using linux, you can install figlet by apt:
sudo apt-get install figlet
```
6. modify the parameter in `deploy.sh` file to your own
```shell
python main.py \
--cutoff $before_when_you_would_never_get_up_but_stay_up_late(float) \
--getup_threshold $time_you_should_get_up(float) \
--recent_days $how_many_day_you_want_to_show_details_of_get-up \
--name $your_name
```
7. modify the infomation in `personal_info.yml` file to your own
8. give workflow Read and write permissions:
![image](./pic/workflow-permisson-1.png)
![image](./pic/workflow-permisson-2.png)
9. set shortcut in your laptop to run the `getup.sh` command: add this in your `~/.bashrc` if you use bash, or add it in your `~/.zshrc` if you use zsh.
```shell
alias getup="cd $project_position; bash getup.sh"
```
10. run the following command to generate get-up data:
```shell
bash getup.sh
```
11. set the github page to the `gh-pages` branch
![image](./pic/github-page.png)
Congratulations! now you can open your terminal and type `getup` to document your get-up time! after that, there will be a train running in your terminal to celebrate your get-up!:
![image](./pic/terminal-sl.png)
![image](./pic/terminal-morning.png)
![image](./pic/github-page-preview.png)



