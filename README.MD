![logo fingerdig](https://imgur.com/3lv49CT.png)
# 

Fingerdig retrieve thumbprint from https connections to IoT devices. 

ESP32, ESP8266, Arduino among other devices, to carry out https requests they need the fingerprint of the site, which is often manually placed in the code and when they expire, the programmer will have to put it again.

Then the fingerdig appears to supply the need and provide via api the fingerprint of the website, SHA1, MD5 or SHA256.

## Usage

Use the website [http://fingerdig.heroku.com](http://fingerdig.heroku.com) to http request.



```code
# get all fingerprints
http://fingerdig.heroku.com/fingerprint
```

```code
# get only fingerprint md5
http://fingerdig.heroku.com/fingerprint/md5
```

```code
# get only fingerprint sha1
http://fingerdig.heroku.com/fingerprint/sha1
```

```code
# get only fingerprint sha256
http://fingerdig.heroku.com/fingerprint/sha256
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)