package main

import (
	"github.com/emersion/go-imap"
	"github.com/emersion/go-imap/client"
	"log"
)

func main() {
	var c *client.Client

	server := "imap.qiye.aliyun.com:993"
	email := "hr@jiewen.com.cn"
	password := "Aisino-2098"

	//server := "imap.qq.com:993"
	//email := "977918953@qq.com"
	//password := "hnlazedlakohbfjg"

	folder := "INBOX"

	var err error
	c, err = client.DialTLS(server, nil)
	if err != nil {
		log.Println("dial", err)
	}
	err = c.Login(email, password)
	if err != nil {
		log.Println("login", err)
	}
	log.Println("client", c, folder)

	mbox, err := c.Select(folder, true)
	if err != nil {
		log.Println("select", err)
	}

	//criteria := imap.NewSearchCriteria()
	//criteria.SeqNum =
	//ids, err := c.Search(criteria)
	//log.Println("search", err)
	//log.Println("ids", ids)

	var from, to uint32
	from = uint32(1)
	to = mbox.Messages

	seqset := new(imap.SeqSet)
	seqset.AddRange(from, to)

	criteria := imap.NewSearchCriteria()
	criteria.SeqNum = seqset
	ids, err := c.Search(criteria)
	log.Println("search", err)
	log.Println("ids", ids)

	messages := make(chan *imap.Message, 100)
	done := make(chan error, 1)
	var section imap.BodySectionName
	go func() {
		done <- c.Fetch(seqset, []imap.FetchItem{section.FetchItem()}, messages)
	}()
	for msg := range messages {
		func() {
			r := msg.GetBody(&section)
			if r == nil {
				panic("Server didn't returned message body")
			}
			log.Println("msg", msg.SeqNum, msg.Uid)
		}()
	}
	if err := <-done; err != nil {
		log.Println(email, "读取邮件错误:", err)
	}
}