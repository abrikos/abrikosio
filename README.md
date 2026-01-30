# Example of integration Django templates, DRF and Nuxt

## It needs for fill actual SEO meta tags

### Key principes:

- Nuxt generates bundle into Django's static dir
- - Then moves *index.html*  into Django templates folder
- Django creates routes equivalent to Nuxt routes 
- - That routes always render *index.html*
- - Meta tags filled by context in template render 