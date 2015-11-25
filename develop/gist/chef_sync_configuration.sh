#!/bin/bash

KEY="~/bbmobile_chef/dev/jenkins-dev.pem"
USER="jenkins"

knife cookbook test -a  -o cookbooks/
foodcritic cookbooks/ -f any

for region in dev-vir dev-fra dev-sin
do
	echo "Now syncing $region."
    knife upload cookbooks environments roles data_bags --force -k $KEY -u $USER --chef-repo-path . -s https://chef-$region.mobile.medu.com/organizations/bbmobile
    echo "{\"chef\":{\"chef_server_url\": \"https://chef-$region.mobile.medu.com/organizations/bbmobile\",\"node_name\":\"jenkins\",\"client_key\": \"/home/ubuntu/bbmobile_chef/dev/jenkins-dev.pem\" }}" > /home/ubuntu/.berkshelf/dev-config.json
    
    echo "Starting berks upload process."
	for bfile in $(find cookbooks -name Berksfile); do echo "Uploading $bfile"; berks install -b $bfile -o thirdparty; berks upload -o thirdparty -b $bfile -c /home/ubuntu/.berkshelf/dev-config.json --no-ssl-verify; done
    echo ""
    echo ""
done

# Clear berkshelf config.
echo "" > /home/ubuntu/.berkshelf/dev-config.json

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "All Chef data synced from stash.bbpd.io/mops/cookbooks.git to Chef servers at Virginia(vir), Frankfurt(fra) and Singapore(sin)."
