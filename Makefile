install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-progression

.PHONY: install brain-games build publish package-install reinstall lint brain-even brain-calc brain-gcd brain-progression brain-prime
