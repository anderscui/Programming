package main

import (
	"encoding/json"
	//"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
)

type Basic struct {
	Address      interface{} `json:"address"`
	Age          interface{} `json:"age"`
	Birthday     interface{} `json:"birthday"`
	ChineseId    interface{} `json:"chinese_id"`
	Degree       interface{} `json:"degree"`
}

var MysqlPool *sqlx.DB

func main() {
	dsn := fmt.Sprintf("root:nadileaf@tcp(10.10.10.200:3306)/Email_Cvparse?charset=utf8mb4&parseTime=True")
	db, err := sqlx.Connect("mysql", dsn)
	if err != nil {
		log.Println("open mysql failed,", err)
	}
	MysqlPool = db
	MysqlPool.SetMaxOpenConns(30)
	MysqlPool.SetMaxIdleConns(30)

	conn, _ := MysqlPool.Beginx()
	sql := `create table if not exists email_candidate
           (
               id         varchar(256) primary key,
               main	    varchar(256)        not null,
               channel    varchar(256)        not null,
               position   varchar(256)        not null,
               resume     json                not null,
               email_time timestamp           not null,
               status     int       default 0 not null,
               content    longblob            not null,
               create_at  timestamp default now(),
               update_at  timestamp default NOW(),
               fulltext email_index (main),
               fulltext position_index (position)
           ) charset utf8mb4;`

	_, err = conn.Exec(sql)
	if err != nil {
		_ = conn.Rollback()
	}
	_ = conn.Commit()

	insertInto()
}

func insertInto() {
	defer func() {
		if err := recover(); err != nil {
			log.Println("defer error:", err)
		}
	}()

	var sql string
	sql = `insert into email_candidate (id, main, channel, position, resume, content, email_time)
				VALUES (?,?,?,?,?,?,?)
				on duplicate key update channel=values(channel),
                        position=values(position),
                        resume=values(resume),
                        content=values(content),
                        email_time=values(email_time),
                        update_at=now();`

	basic := Basic {
		Address: "sh",
		Age: 20,
		ChineseId: "123456",
		Degree: 16,
	}
	data, _  := json.Marshal(basic)
	content := []byte("abcabcabcabc")

	conn, _ := MysqlPool.Beginx()
	_, err := conn.Exec(sql, "123", "resume", "51", "工程师", data, content, nil)
	if err != nil {
		_ = conn.Rollback()
		log.Println("insert error:", err)
	} else {
		_ = conn.Commit()
		log.Println("insert ok:", err)
	}
}