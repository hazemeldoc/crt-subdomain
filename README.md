# crt subdomain
## idea
- the tool find subdomain from crt.sh website which help pentester and bug hunters to extract subdomains without wasting time on reading the result from actual website

>the tool extact subdomains , sort them and analyze which of the subdomains are alive

## usage
```
python3 crt_sh.py -d <domain> [flags]
args:
    <domain> : enter the name of the domain to scan eg:google.com
flags:
    -a       : show only alive subdomains
```
## installation
```
git clone 
pip3 install -r requirements.txt
```
## sample run
![RUN](https://github.com/hazemeldoc/crt-subdomain/raw/master/img/crt_sh-git.gif)
