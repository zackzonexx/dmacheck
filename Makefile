.PHONY: build push

export CI_REGISTRY     ?= <your-registry-link>
export CI_PROJECT_PATH ?= <your-project-path>

CHECKER_IMAGE            = $(CI_REGISTRY)/$(CI_PROJECT_PATH)/checker
CHECKER_VERSION         ?= 1.1.0

build:
	docker build -t $(CHECKER_IMAGE):$(CHECKER_VERSION) -f ./deploy/Dockerfile .

push:
	docker push $(CHECKER_IMAGE):$(CHECKER_VERSION)

check:
	@./package/main.py
