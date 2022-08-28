use geekabin;

create table users
(
  user_id int not null
  auto_increment primary key comment 'user id',
        user_email varchar
  (255) not null comment 'user email',
        user_password char
  (100) not null comment 'user password',
        date_created datetime not null default current_timestamp comment 'date created',
        date_updated datetime not null default current_timestamp on
  update current_timestamp comment 'date updated',
        clearance int
  not null default 0 comment 'user clearance',
        user_status int not null default 1 comment 'user status',
        is_potential_threat bool not null default false comment 'is potential threat'
) comment 'manage users';


  create unique index email
    on users (user_id, user_email)
    comment 'with_email';