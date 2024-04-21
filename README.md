<div align="center">
  <img src="https://www.thestoryoftexas.com/upload/images/events/movies/venomwisp-banner.png">
</div>
# Welcome to the LOCAL DATABASE

## Installation

To install the current release of LOCAL DATABASE, please follow of the method described below.


## 1. Clone the GitHub repository:

```shell
git clone https://github.com/VENOM-PROGRAMMING/DATABASE.git
```

## 2. Install dependencies

```shell
pip install -r requirements.txt
```
or
```shell
pip3 install -r requirements.txt
```

## 3. Configure settings

  a) edit port here : `app.run(debug=True, host='0.0.0.0', port=1111)` line `56`
  

## 4. Configure NODE JS
```shell
https://nodejs.org/dist/v20.12.2/node-v20.12.2-linux-x64.tar.xz
```

```shell
tar -xvf node-v20.12.2-linux-x64.tar.xz
```

```shell
export PATH=/usr/local/node-v20.12.2-linux-x64/bin:$PATH

```
```shell
node -v
```
```shell
npm -v
```
## 5. Installing PM2
```shell
npm install pm2 -g
```

## 6. Start an application
You can start any application (Node.js, Python, Ruby, binaries in $PATH...) like that:
```shell
pm2 start main.py
```
ok 

```shell
pm2 start main.py --interpreter python3
```
or
```shell
pm2 start main.py --interpreter python
```
## 7. To list all running applications:
```shell
pm2 list
```

<div align="center">
  <img src="https://github.com/Unitech/pm2/raw/master/pres/pm2-ls-v2.png">
</div>


## 8. Managing apps is straightforward:
```shell
$ pm2 stop     <app_name|namespace|id|'all'|json_conf>
$ pm2 restart  <app_name|namespace|id|'all'|json_conf>
$ pm2 delete   <app_name|namespace|id|'all'|json_conf>
```
Finally!



