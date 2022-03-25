FROM squidfunk/mkdocs-material:latest as develop
# We build a image that is capable to serve our contents (with all dependencies installed)
# You can use this build-phase as a live development server
#  Just mount your documentation into the /docs Directory.

COPY requirements.txt /docs/requirements.txt
RUN pip install -r requirements.txt && rm -f /docs/requirements.txt
COPY includes/abbreviations.md /docs/includes/abbreviations.md
COPY mkdocs.yml /docs/mkdocs.yml
COPY docs /docs/docs

FROM develop as builder
# We build our documentation here, the generated static contents will be copied
# into our nginx container to be served.
RUN mkdocs build --verbose --clean --config-file ./mkdocs.yml


FROM nginx:latest as production

# Now we copy the generated documentation into our nginx container
COPY --from=builder /docs/site /usr/share/nginx/html
