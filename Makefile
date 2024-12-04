generate-client:
	npx @openapitools/openapi-generator-cli version-manager set 7.10.0
	npx @openapitools/openapi-generator-cli generate \
	-g python \
	-i https://raw.githubusercontent.com/DakCrowder/flightctl/567ae4dae416eb375c0afac345de1cc9d845ba44/api/v1alpha1/openapi.yaml \
	-o . \
	--additional-properties=packageName=flightctl \
	--git-user-id flightctl \
	--git-repo-id python-client
