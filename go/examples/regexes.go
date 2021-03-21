package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strings"
)

func ReadText(filePath string) string {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	return string(data)
}

func main() {
	//RE_PHONE_WITH_EXT := regexp.MustCompile(`^\d{11}(\s*转\s*\d{3,5})?$`)
	//fmt.Println(RE_PHONE_WITH_EXT.MatchString("a18501968044"))
	//fmt.Println(RE_PHONE_WITH_EXT.MatchString("18501968044"))
	//fmt.Println(RE_PHONE_WITH_EXT.FindString("18501968044"))
	//fmt.Println(RE_PHONE_WITH_EXT.MatchString("18501968044转1964"))
	//fmt.Println(RE_PHONE_WITH_EXT.FindString("18501968044转1964"))
	//
	//RE_WHITESPACE := regexp.MustCompile(`\s+`)
	//fmt.Println(RE_WHITESPACE.ReplaceAllString("a  b\tcd\ne", ""))

	//text := ReadText("data/liepin_email_2.txt")
	//RE_LIEPIN_CONTACT := regexp.MustCompile(`(?i)href="(.*?.(liepin|lietou-edm).com.*?)".*?>联系目标人选`)
	//matches := RE_LIEPIN_CONTACT.FindStringSubmatch(text)
	//contactUrl := matches[1]
	//contactUrl = strings.Replace(contactUrl, "amp;", "", -1)
	//fmt.Println(contactUrl)

	text := ReadText("data/bjx_email_1.txt")
	RE_BJX_CONTACT := regexp.MustCompile(`(?i)href="(.*?.bjx.com.*?)".*?>我要联系`)
	matches := RE_BJX_CONTACT.FindStringSubmatch(text)
	contactUrl := matches[1]
	contactUrl = strings.Replace(contactUrl, "amp;", "", -1)
	fmt.Println(contactUrl)
}