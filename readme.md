Get a chalice app validating a [reCAPTCHA](https://developers.google.com/recaptcha/intro) test.

Sign up for an [API key](http://www.google.com/recaptcha/admin).  After you deploy you'll need to come back here an update the domains.  For now just add `localhost` as a domain.

The application expects environment variables `RECAPTCHA_SITE_KEY` and `RECAPTCHA_SECREY_KEY`.  You can set these in `.chalice/config.json`.  Is there a better way to externalize these so I don't check them into git?

```bash
pip3 install -r requirements.txt
chalice local
```

You can play with the site locally.  Then `chalice deploy`, get the domain from API gateway, e.g. `1234567890.execute-api.us-east-1.amazonaws.com`, add this to the domains in your [reCAPTCHA settings](http://www.google.com/recaptcha/admin).
