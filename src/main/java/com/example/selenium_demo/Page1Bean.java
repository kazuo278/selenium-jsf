package com.example.selenium_demo;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import com.example.selenium_demo.dto.Item;

import jakarta.annotation.PostConstruct;
import jakarta.faces.context.ExternalContext;
import jakarta.faces.view.ViewScoped;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.inject.Inject;
import jakarta.inject.Named;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.Setter;

@Named
@ViewScoped
public class Page1Bean implements Serializable {

  @Inject
  ExternalContext context;

  @Getter
  List<Item> itemList;

  @Getter
  String userAgent;

  @Getter
  @Setter
  @NotEmpty(message = "品名を入力してください")
  String newItemName;

  @Getter
  @Setter
  @Min(value = 1, message = "個数は1以上の整数を指定してください")
  @NotNull(message = "個数を入力してください")
  Integer newItemAmount;

  @PostConstruct
  public void init() {
    // サンプル初期データの作成
    itemList = new ArrayList<>();
    Item apple = new Item("りんご", 10);
    Item melon = new Item("メロン", 3);
    itemList.add(apple);
    itemList.add(melon);
    // ユーザエージェントの取得
    HttpServletRequest request =(HttpServletRequest)context.getRequest();
    this.userAgent = request.getHeader("user-agent");
  }

  public void addItem() {
    // itemの追加
    System.out.println("品名：" + newItemName);
    System.out.println("個数：" + newItemAmount);
    Item newItem = new Item();
    newItem.setName(newItemName);
    newItem.setAmount(newItemAmount);
    itemList.add(newItem);
    // 入力フォームの初期化
    newItemName = null;
    newItemAmount = null;
  }
}