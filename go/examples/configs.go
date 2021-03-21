package main

import (
	"strings"
)

type TslCert struct {
	privateKeyFile string
	certificateFile string
}

func main() {
	rawConfig := "mail.ciicsh.com:email_client.pem,email_client.key"

	configs := strings.Split(rawConfig, ";")
	certConfigs := make(map[string]TslCert)
	for _, config := range configs {
		configParts := strings.Split(config, ":")
		if len(configParts) == 2 {
			server := configParts[0]
			certParts := strings.Split(configParts[1], ",")
			if len(certParts) == 2 {
				keyFile := certParts[0]
				certFIle := certParts[1]
				certConfigs[server] = TslCert{privateKeyFile: keyFile, certificateFile: certFIle}
			}
		}
	}
	fm
}