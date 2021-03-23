# rtx 3090 stock checker for newegg

This project is super simple and highly unoptomized
I created this project to test my understanding and usage of def statments, requests, and a few other tests for future projects.

# How it works:

Bascilly it pulls data from a specifc product page (in this case a newegg product page eg: https://www.newegg.com/zotac-geforce-rtx-3090-zt-a30900d-10p/p/N82E16814500503?Description=rtx%203090&cm_re=rtx_3090-_-9SIANCVDU88863-_-Product

Checks to see if the page contains ("OUT OF STOCK") or if it contains ("In stock") and displays info needed depending on that result
If the page contains "In stock" then I append the things in stock to a list for later output

# Other info:

This is easily expandable and at some point I'd like to be able to pull the price of things by parsing the data.

I may also add more links and expand this to different sites as well.
