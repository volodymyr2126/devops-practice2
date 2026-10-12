FROM golang:tip-alpine3.23 AS first_stage
WORKDIR /app
COPY script.go .
RUN go build -o bin/script script.go

FROM scratch
COPY --from=first_stage /app/bin/script /app/script
CMD ["/app/script"]