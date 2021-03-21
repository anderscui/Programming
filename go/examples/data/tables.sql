create table if not exists email_account
(
    id          int auto_increment 	  primary key,
    domain	    varchar(256)    	  	  not null,
    email       varchar(256)           not null,
    password    varchar(256)           not null,
    protocol    varchar(256)           not null,
	`ssl`      boolean                not null,
	create_at   timestamp              not null default now(),
    update_at   timestamp              not null default now(),

    unique index account_index (domain, email)
) charset utf8mb4;

------SEP------
create table if not exists email_account_status
(
    domain	   varchar(256)    	  	  not null,
    email       varchar(256)           not null,
    status      varchar(256)           not null,
    sleep_until bigint                 not null,
    create_at   timestamp              not null default now(),
    update_at   timestamp              not null default now(),

    primary key (domain, email)
) charset utf8mb4;

------SEP------
create table if not exists email_task
(
    mail_id	   		varchar(256)    	  	  not null,
    mail_time 		timestamp           	  not null,
    account_id  		int 	   	   		   	  not null,
    status      		varchar(256)           	  not null,
    should_retry   	boolean                	  not null,
    times_retried   	int                	  	  not null default -1,
    parser_version   varchar(256)		      null,
    create_at   	 	timestamp              	  not null default now(),
    update_at   		timestamp              	  not null default now(),

    primary key (mail_id)
) charset utf8mb4;