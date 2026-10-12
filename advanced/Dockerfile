FROM python:3.14-alpine

ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_PORT=8050

RUN apk add --no-cache curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/app/.venv/bin:/root/.local/bin:$PATH"
WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./
RUN uv sync --locked --no-dev --no-install-project
EXPOSE 8050

COPY src ./src
CMD ["uv", "run", "streamlit", "run", "src/local_chat_bot_proj/app.py", "--server.address=0.0.0.0", "--server.port=8050"]
