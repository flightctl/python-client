generate-client:
	npx @openapitools/openapi-generator-cli version-manager set 7.10.0
	npx @openapitools/openapi-generator-cli generate \
	-g python \
	-i https://raw.githubusercontent.com/flightctl/flightctl/6f52768c6786bef07605a59ad422219181542332/api/v1alpha1/openapi.yaml \
	-o . \
	--additional-properties=packageName=flightctl \
	--git-user-id flightctl \
	--git-repo-id python-client
