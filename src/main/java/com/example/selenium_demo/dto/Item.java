package com.example.selenium_demo.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Item {
  /**
   * 品名
   * 
   * @param name 品名
   * @return 品名
   */
  String name;
  /**
   * 個数
   * 
   * @param amount 個数
   * @return 個数
   */
  Integer amount;

  /**
   * コンストラクタ
   */
  public Item() {
  }

  /**
   * コンストラクタ
   * 
   * @param name   品名
   * @param amount 個数
   */
  public Item(String name, Integer amount) {
    this.name = name;
    this.amount = amount;
  }
}