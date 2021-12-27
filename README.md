# Replace secrets for Googles App Engine Deployment

If you are using Googles App Engine and want to use secrets in the `app.yaml` file, you can store them as Secrets in
your repository and have them replaced during deployment.

[![Test-Workflow](https://github.com/73h/gae-app-yaml-replace-env-variables/actions/workflows/main.yaml/badge.svg)](https://github.com/73h/gae-app-yaml-replace-env-variables/actions/workflows/main.yaml)

---

## Usage

Place the following in your `/.github/workflows/main.yml` behind `actions/checkout@v2`.

```yml
...
steps:
  - uses: actions/checkout@v2
  - uses: 73h/gae-app-yaml-replace-env-variables@v0.1
    env:
      SECRET_ONE: ${{ secrets.SECRET_ONE }}
      ANOTHER_SECRET: ${{ secrets.ANOTHER_SECRET }}
    with:
      app_yaml_path: "app.yaml"
...
```

Extract `app.yaml`

```yml
...
env_variables:
  APP_ENV: production
  SECRET_ONE: $SECRET_ONE
  ANOTHER_SECRET: $ANOTHER_SECRET
...
```

### Full Example with Google's App Engine

An example with Google's App Engine (GAE) deployment.

`/.github/workflows/main.yml`

```yml
on: push
name: Deploy site on push
jobs:
  deploy_on_googles_app_engine:
    name: Deploy
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: 73h/gae-app-yaml-replace-env-variables@v0.1
        env:
          SECRET_ONE: ${{ secrets.SECRET_ONE }}
          SECRET_TWO: ${{ secrets.SECRET_TWO }}
        with:
          app_yaml_path: "app.yaml"
      - uses: 'google-github-actions/auth@v0'
        with:
          credentials_json: '${{ secrets.GCP_SA_JSON }}'
      - uses: 'google-github-actions/deploy-appengine@v0'
        with:
          deliverables: 'app.yaml'
          promote: true
          version: 'v1'
```

The full `app.yaml` file looks like this.

```yml
runtime: python39
entrypoint: gunicorn -b :$PORT main:app --chdir app
handlers:
  - url: /.*
    script: auto
    secure: always
    redirect_http_response_code: 301
automatic_scaling:
  max_instances: 1
env_variables:
  APP_ENV: production
  SECRET_ONE: $SECRET_ONE
  SECRET_TWO: $SECRET_TWO
  ANOTHER_PARAM: "73"
```

---

### Settings

| Key Name | Required | Examples | Default Value | Description |
|---|---|---|---|---|
| `app_yaml_path` | No | `config/app.yaml`<br />`myapp.yaml` | `app.yaml` | full path to your app.yaml file |

---

