# Website

## Write

```
bundle exec jekyll post "My New Post"
```

## Run

```
bundle exec jekyll serve --livereload
```

## Run with Docker

```
docker run \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  jekyll serve --livereload
```
