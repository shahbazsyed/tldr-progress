export TYPESENSE_API_KEY="e5570aa0-5d05-4246-bdef-a74705a44d0a"
docker run -p 8108:8108 -v/typesense-data:/data typesense/typesense:0.20.0 \
  --data-dir /data --api-key=$TYPESENSE_API_KEY