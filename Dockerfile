FROM node:21.7.1-alpine AS cssbuild

WORKDIR /app

COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && \
 pnpm install

COPY ./ /app
COPY tailwind.config.js ./
RUN pnpm run build
CMD ["pnpm", "run", "watch"]

FROM ghcr.io/trojsten/django-docker:v4

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root


USER appuser

COPY --chown=appuser:appuser ./ /app

COPY --from=cssbuild /app/seminare/style/static/* /app/seminare/style/static/

RUN DATABASE_URL=sqlite://:memory: python manage.py collectstatic --no-input
ENV BASE_START=/app/entrypoint.sh
