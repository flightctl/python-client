generate-client:
	npx @openapitools/openapi-generator-cli version-manager set 7.10.0
	npx @openapitools/openapi-generator-cli generate \
	-g python \
	-i https://raw.githubusercontent.com/DakCrowder/flightctl/0187407828e9ab5194aadf5c14e502fbe4923894/api/v1alpha1/openapi.yaml \
	-o . \
	--additional-properties=packageName=flightctl \
	--git-user-id flightctl \
	--git-repo-id python-client
