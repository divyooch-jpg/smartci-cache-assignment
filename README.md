# SmartCI - Smart Build-Cache Invalidation

Assignment 4\_2 (Automation in Software Development).
A small Python project whose GitHub Actions workflow caches pip downloads.
The cache key is pip-<hash of requirements.txt>, so editing requirements.txt
invalidates the cache automatically, and leaving it alone reuses it.

See .github/workflows/ci.yml. hi i am divyansh chaudhary

