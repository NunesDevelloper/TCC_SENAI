# ====== backend ====== 
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \

WORKDIR /backend

COPY ./backend/requirements.txt /backend/

RUN pip install --no-cache-dir -r requirements.txt
COPY ./backend/ /backend/

RUN chmod +x /backend/entrypoint.sh

#toda fez que o docker for estardo ele vai e roda esse script
ENTRYPOINT ["/backend/entrypoint.sh"]

EXPOSE 8000

RUN cd /backend/src

CMD ["uvicorn", "setting.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

RUN cd /


# ====== frontend - bild ====== 
FROM node:20

WORKDIR /frontend

COPY ./frontend/package*.json /frontend/

RUN npm run build

# ====== frontend - expose ====== 
FROM nginx:alpine

COPY --from=build /frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
