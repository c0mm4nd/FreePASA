cd frontend
npm i
npm run build
cp dist/index.html ../backend/templates
cp dist/* ../backend/static

cd ../backend
python server.py