Please rename example.env to .env and fill unfilled variables


flask db init
flask db migrate -m "users table"
flask db upgrade
flask db downgrade
