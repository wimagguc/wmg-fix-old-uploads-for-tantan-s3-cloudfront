# FIX OLD tantan-s3-cloudfront UPLOADS

Tantan's Amazon S3 plugin is pretty great for Wordpress. Unfortunately you can't use it with a massive existing library, which is what this script takes care of.

## Usage

1. Create your Amazon bucket, and set up Amazon S3 plugin as usual

2. Upload all the files to /wp-content/uploads/... folder within the bucket and make them public. (I'm usually using Cyberduck for this, it's pretty straight forward.)

3. Change the settings.py and run the script in this repository.

## Prerequisites

* Python
* MySQL driver for Python
* Access to the MySQL DB (*Double-check with MySQL Workbench before adding a ticket here, please*)
* Wordpress with tantan-s3-cloudfront set up

## Before you run the script: Virtualenv & requirements

```sh
$ virtulenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run

```sh
$ source venv/bin/activate
$ python script.py
```

## License

[MIT, do-with-the-code-whatever-you-please License](https://github.com/wimagguc/wmg-fix-old-uploads-for-tantan-s3-cloudfront/blob/master/LICENSE)

## About

Richard Dancsi

- Blog: [wimagguc.com](http://www.wimagguc.com/)
- Github: [github.com/wimagguc](http://github.com/wimagguc/)
- Twitter: [twitter.com/wimagguc](http://twitter.com/wimagguc/)
- Linkedin: [linkedin.com/in/richarddancsi](http://linkedin.com/in/richarddancsi)