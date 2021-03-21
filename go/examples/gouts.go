package main

import (
	"fmt"
	"github.com/guonaihong/gout"
	"log"
	"time"
)

type SiteAuthConfig struct {
	UserName string `json:"username"`
	Password string `json:"password"`
	Cookie string `json:"cookie"`
}

type GeneralContact struct {
	Email  string `json:"email"`
	Phone string `json:"phone"`
	Msg string `json:"msg"`
	Status int32 `json:"status"`
}

type GeneralContactRes struct {
	Authorization  string `json:"Authorization"`
	Contact GeneralContact `json:"data"`
	Msg string `json:"msg"`
	Status int32 `json:"status"`
}

func getOrigin(channel string) string {
	siteOrigins := map[string]string{
		"北极星": "hr.bjx.com.cn",
		"猎聘": "liepin.com",
	}

	origin, ok := siteOrigins[channel]
	if ok {
		return origin
	} else {
		return "未知"
	}
}

func GetGeneralContact(channel, url string, auth SiteAuthConfig) GeneralContactRes {
	var (
		resp   GeneralContactRes
		errStr string
		code   int
	)
	origin := getOrigin(channel)
	log.Println("origin:", origin)
	err := gout.POST(fmt.Sprintf("http://localhost:5679/getContact2")).
		Debug(false).
		SetForm(gout.H{
			"url":      url,
			"origin":   origin,
			"username": auth.UserName,
			"password": auth.Password,
		}).
		Callback(func(c *gout.Context) (err error) {
			switch c.Code {
			case 200:
				c.BindJSON(&resp)
			default:
				c.BindBody(&errStr)
			}
			return nil
		}).
		SetTimeout(time.Duration(10) * time.Second).
		Code(&code).
		Filter().
		Retry().
		Attempt(1).
		WaitTime(2 * time.Second).
		Do()

	if err != nil {
		log.Println("GetZhilianContact Error:", err)
		return GeneralContactRes{Status: -1}
	} else if code == 200 {
		return resp
	}
	log.Println("GetZhilianContact failed:", code, errStr)
	return GeneralContactRes{Status: -1}
}

func main() {
	auth := SiteAuthConfig{UserName: "运达风电", Password: "ydzp8739"}
	contact := GetGeneralContact("北极星",
		"https://yun.bjx.com.cn/resume/details?oid=28297554&rnum=031F50DB6563251D&rank=1&type=1&dir=0",
		    auth)
	log.Println(contact.Contact)
}