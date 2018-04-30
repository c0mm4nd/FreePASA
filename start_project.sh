cd frontend
npm i
npm run build
mkdir ../backend/templates && cp dist/index.html ../backend/templates
mkdir ../backend/static && cp dist/* ../backend/static

cd ../backend
python server.py