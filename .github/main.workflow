workflow "Purge cache on page build" {
  resolves = ["Send purge command"]
  on = "page_build"
}

action "Send purge command" {
  uses = "swinton/httpie.action@02571a073b9aaf33930a18e697278d589a8051c1"
  secrets = ["CF_ZONE", "CF_KEY", "CF_EMAIL"]
  args = ["https://api.cloudflare.com/client/v4/zones/$CF_ZONE/purge_cache", "X-Auth-Email:$CF_EMAIL", "X-Auth-Key:$CF_KEY", "purge_everything:=true"]
}
